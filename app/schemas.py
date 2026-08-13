from pydantic import BaseModel, Field


class CommentRequest(BaseModel):
    platform: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Social media platform, e.g. reddit or linkedin"
    )

    post_title: str = Field(
        ...,
        min_length=3,
        max_length=300,
        description="Title of the social media post"
    )

    post_content: str = Field(
        ...,
        min_length=5,
        max_length=10000,
        description="Content of the social media post"
    )

    community: str | None = Field(
        default=None,
        max_length=100,
        description="Community or subreddit name"
    )


class CommentResponse(BaseModel):
    platform: str
    comment: str