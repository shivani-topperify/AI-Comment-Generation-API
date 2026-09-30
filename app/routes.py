from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.llm import generate_comment
from app.models import Comment
from app.prompts import build_comment_prompt
from app.schemas import CommentRequest, CommentResponse

router = APIRouter()


@router.post("/generate-comment", response_model=CommentResponse)
def generate_comment_endpoint(
    request: CommentRequest,
    db: Session = Depends(get_db)
):
    try:
        prompt = build_comment_prompt(
            platform=request.platform,
            post_title=request.post_title,
            post_content=request.post_content,
            community=request.community
        )

        print("STEP 1: Prompt created")

        comment = generate_comment(prompt)

        print("STEP 2: Gemini generated comment")

        new_comment = Comment(
            platform=request.platform,
            community=request.community,
            post_title=request.post_title,
            post_content=request.post_content,
            generated_comment=comment
        )

        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)

        print("STEP 3: Comment saved to database")

        return {
            "platform": request.platform,
            "comment": comment
        }

    except Exception as e:
        db.rollback()

        print("ERROR TYPE:", type(e).__name__)
        print("ERROR MESSAGE:", str(e))

        raise HTTPException(
            status_code=500,
            detail="Unable to generate and save comment at the moment."
        )


@router.get("/comments")
def get_comments(db: Session = Depends(get_db)):
    comments = db.query(Comment).all()
    return comments


@router.get("/comments/{comment_id}")
def get_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):
    comment = (
        db.query(Comment)
        .filter(Comment.id == comment_id)
        .first()
    )

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    return comment


@router.delete("/comments/{comment_id}")
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db)
):
    comment = (
        db.query(Comment)
        .filter(Comment.id == comment_id)
        .first()
    )

    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    db.delete(comment)
    db.commit()

    return {
        "message": "Comment deleted successfully",
        "id": comment_id
    }