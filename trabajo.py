

import streamlit as st
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional

# 1. Define SQLModel Class based on the SQL Schema
class CursoInformatica(SQLModel, table=True):
    __tablename__ = "curso_informatica"
    __table_args__ = {"extend_existing": True}

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre_modulo: str
    horas: int
    indice: str

# 2. Define Database File and Engine
DATABASE_FILE = "database.db"
engine = create_engine(f"sqlite:///{DATABASE_FILE}")

# 3. Function to Create Database and Tables
def create_db_and_tables():
    """
    Creates the database and all tables defined by SQLModel metadata.
    """
    SQLModel.metadata.create_all(engine)

# 4. Function to Populate Database with Sample Data
def populate_database():
    """
    Adds sample records to the database tables if they are empty.
    """
    with Session(engine) as session:
        # Check if the table is already populated
        if not session.exec(select(CursoInformatica)).first():
            curso1 = CursoInformatica(
                nombre_modulo="Introducción a Python",
                horas=40,
                indice="PY-01"
            )
            curso2 = CursoInformatica(
                nombre_modulo="Bases de Datos con SQL",
                horas=35,
                indice="DB-01"
            )
            curso3 = CursoInformatica(
                nombre_modulo="Desarrollo Web con Streamlit",
                horas=50,
                indice="WEB-01"
            )

            session.add(curso1)
            session.add(curso2)
            session.add(curso3)
            session.commit()

# 5. Main Streamlit Application Function
def main():
    """
    The main function for the Streamlit application.
    """
    st.set_page_config(page_title="Gestor de Cursos", layout="wide")
    st.title("Gestor de Cursos de Informática")
    st.markdown(
        "Esta aplicación muestra los módulos de un curso de informática "
        "almacenados en una base de datos SQLite."
    )

    # Create database and tables on first run
    create_db_and_tables()

    with Session(engine) as session:
        # Check if data exists, if not, populate it
        if not session.exec(select(CursoInformatica)).first():
            populate_database()
            st.success("Base de datos poblada con datos de ejemplo.")
            # Rerun to display the new data immediately
            st.rerun()

        # Display data for the table
        st.subheader("Módulos del Curso de Informática")
        cursos = session.exec(select(CursoInformatica)).all()
        if cursos:
            # Convert list of model objects to a list of dicts for display
            cursos_dict = [c.model_dump() for c in cursos]
            st.dataframe(cursos_dict, use_container_width=True)
        else:
            st.warning("No hay datos en la tabla 'curso_informatica'.")

if __name__ == "__main__":
    main()
