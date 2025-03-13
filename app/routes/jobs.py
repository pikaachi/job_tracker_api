from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.auth_handler import get_current_user  # Import fixed get_current_user

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=schemas.JobResponse)
def create_job(
    job: schemas.JobCreate, 
    db: Session = Depends(database.get_db), 
    user: models.User = Depends(get_current_user)  # Uses username
):
    """Create a new job application (Authenticated users only)."""

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )


    # Create job entry
    new_job = models.JobApplication(
        company=job.company,
        position=job.position,
        status=job.status,
        user_id=user.id  # Uses the ID of the authenticated user
    )

    try:
        db.add(new_job)
        db.commit()
        db.refresh(new_job)

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

    return new_job

@router.get("/", response_model=list[schemas.JobResponse])
def get_jobs(
    db: Session = Depends(database.get_db), 
    user: models.User = Depends(get_current_user)  # Authenticated user required
):
    """Get all job applications for the logged-in user."""

    #print(f"✅ Fetching jobs for user: {user.username}")  # Debugging log

    jobs = db.query(models.JobApplication).filter(models.JobApplication.user_id == user.id).all()

    #print(f"✅ Found {len(jobs)} jobs")  # Debugging log

    return jobs

@router.get("/{job_id}", response_model=schemas.JobResponse)
def get_job_by_id(
    job_id: int,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(get_current_user)  # ✅ Authenticated user required
):
    """Retrieve a specific job application (only the owner can access)."""

    # ✅ Step 1: Fetch the job and ensure the user owns it
    job = db.query(models.JobApplication).filter(
        models.JobApplication.id == job_id,
        models.JobApplication.user_id == user.id  # ✅ Ensure the user owns the job
    ).first()

    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found or not authorized to view"
        )

    print(f"✅ Retrieved Job: {job.__dict__}")  # Debugging log
    return job


@router.put("/{job_id}", response_model=schemas.JobResponse)
def update_job(
    job_id: int,
    job_update: schemas.JobUpdate,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(get_current_user)  # ✅ Authenticated user required
):
    """Update an existing job application (only the owner can update)."""

    #Fetch the job
    existing_job = db.query(models.JobApplication).filter(
        models.JobApplication.id == job_id,
        models.JobApplication.user_id == user.id  # ✅ Ensure the user owns the job
    ).first()

    if not existing_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found or not authorized to update"
        )

    #Update only provided fields
    if job_update.company is not None:
        existing_job.company = job_update.company
    if job_update.position is not None:
        existing_job.position = job_update.position
    if job_update.status is not None:
        existing_job.status = job_update.status

    try:
        db.commit()
        db.refresh(existing_job)

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

    return existing_job
