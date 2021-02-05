"""empty message

Revision ID: d1318af6a970
Revises: 149d598cf92b
Create Date: 2021-02-05 10:40:07.577982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1318af6a970'
down_revision = '149d598cf92b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lecture',
    sa.Column('lectureId', sa.Integer(), nullable=False),
    sa.Column('classId', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('content', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['classId'], ['classes.classId'], ),
    sa.PrimaryKeyConstraint('lectureId')
    )
    op.create_table('quiz',
    sa.Column('quizId', sa.Integer(), nullable=False),
    sa.Column('lectureId', sa.Integer(), nullable=True),
    sa.Column('question', sa.String(length=30), nullable=True),
    sa.Column('answer', sa.String(length=30), nullable=True),
    sa.Column('a1', sa.String(length=30), nullable=True),
    sa.Column('a2', sa.String(length=30), nullable=True),
    sa.Column('a3', sa.String(length=30), nullable=True),
    sa.Column('a4', sa.String(length=30), nullable=True),
    sa.ForeignKeyConstraint(['lectureId'], ['lecture.lectureId'], ),
    sa.PrimaryKeyConstraint('quizId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz')
    op.drop_table('lecture')
    # ### end Alembic commands ###
