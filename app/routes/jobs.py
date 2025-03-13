from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, database
from app.auth_handler import get_current_user  # ✅ Import fixed `get_current_user`

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=schemas.JobResponse)
def create_job(
    job: schemas.JobCreate, 
    db: Session = Depends(database.get_db), 
    user: models.User = Depends(get_current_user)  # ✅ Uses `username` now
):
    """Create a new job application (Authenticated users only)."""

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )

    print(f"✅ Authenticated User: {user.username}")  # Debugging log

    # Create job entry
    new_job = models.JobApplication(
        company=job.company,
        position=job.position,
        status=job.status,
        user_id=user.id  # ✅ Uses the ID of the authenticated user
    )

    try:
        db.add(new_job)
        db.commit()
        db.refresh(new_job)
        print(f"✅ Job successfully created: {new_job.id}")  # Debugging log

    except Exception as e:
        db.rollback()
        print(f"❌ Database error: {str(e)}")  # Debugging log
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

    return new_job

@router.get("/", response_model=list[schemas.JobResponse])
def get_jobs(
    db: Session = Depends(database.get_db), 
    user: models.User = Depends(get_current_user)  # ✅ Authenticated user required
):
    """Get all job applications for the logged-in user."""

    print(f"✅ Fetching jobs for user: {user.username}")  # Debugging log

    jobs = db.query(models.JobApplication).filter(models.JobApplication.user_id == user.id).all()

    print(f"✅ Found {len(jobs)} jobs")  # Debugging log

    return jobs

