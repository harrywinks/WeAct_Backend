"""empty message

Revision ID: ef8a49a0f744
Revises: 
Create Date: 2021-02-05 10:56:10.659872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef8a49a0f744'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classes',
    sa.Column('classId', sa.Integer(), nullable=False),
    sa.Column('className', sa.String(length=20), nullable=True),
    sa.Column('subject', sa.String(length=20), nullable=True),
    sa.Column('tutorId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tutorId'], ['tutor.tutorId'], ),
    sa.PrimaryKeyConstraint('classId')
    )
    op.create_table('tutor',
    sa.Column('tutorId', sa.Integer(), nullable=False),
    sa.Column('pw', sa.String(length=20), nullable=False),
    sa.Column('classId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classId'], ['classes.classId'], ),
    sa.PrimaryKeyConstraint('tutorId')
    )
    op.create_table('lecture',
    sa.Column('lectureId', sa.Integer(), nullable=False),
    sa.Column('classId', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('content', sa.LargeBinary(), nullable=True),
    sa.ForeignKeyConstraint(['classId'], ['classes.classId'], ),
    sa.PrimaryKeyConstraint('lectureId')
    )
    op.create_table('student',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('pw', sa.String(length=20), nullable=False),
    sa.Column('classId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['classId'], ['classes.classId'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('userId')
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
    op.drop_table('student')
    op.drop_table('lecture')
    op.drop_table('tutor')
    op.drop_table('classes')
    # ### end Alembic commands ###
