import datetime
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String, unique=True)
    clave = mapped_column(String)
    email = mapped_column(String)
    movil = mapped_column(String)
    creado = mapped_column(DateTime, default=datetime.datetime.now)
    ultimo_login = mapped_column(DateTime)
    activo = mapped_column(Integer)
    id_empresa = mapped_column(ForeignKey("empresas.id"))
    id_perfil = mapped_column(ForeignKey("perfiles.id"))
    empresa = relationship(back_populates="usuarios")
    perfil = relationship(back_populates="usuarios")

class Empresa(Base):
    __tablename__ = 'empresas'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String)
    nif = mapped_column(String)
    direccion = mapped_column(String)
    provincia = mapped_column(String)
    pais = mapped_column(String)
    registro = mapped_column(String)
    movil = mapped_column(String)
    web = mapped_column(String)
    creado = mapped_column(DateTime, default=datetime.datetime.now)
    usuarios = relationship(back_populates="empresa")

class Perfil(Base):
    __tablename__ = 'perfiles'
    id = mapped_column(Integer, primary_key=True)
    descripcion = mapped_column(String)
    activo = mapped_column(Integer)
    usuarios = relationship(back_populates="perfil")

class Edificio(Base):
    __tablename__ = 'edificios'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String)
    plantas = relationship(back_populates="edificio")

class Planta(Base):
    __tablename__ = 'plantas'
    id = mapped_column(Integer, primary_key=True)
    numero = mapped_column(Integer)
    plano_url = mapped_column(String)
    coordenadas = mapped_column(String)
    id_edificio = mapped_column(ForeignKey("edificios.id"))
    edificio = relationship(back_populates="plantas")

class Dispositivo(Base):
    __tablename__ = 'dispositivos'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String)
    id_tipo_dispositivo = mapped_column(ForeignKey("tipo_dispositivo.id"))


class Estado_dispositivo(Base):
    __tablename__ = 'estado_dispositivo'
    id = mapped_column(Integer, autoincrement=True, primary_key=True)
    nivel_bateria = mapped_column(Integer) 
    humedad = mapped_column(Integer)   
    temperatura = mapped_column(Integer) 
    fecha = mapped_column(DateTime, default=datetime.datetime.now) 
    id_dispositivo = mapped_column(ForeignKey("dispositivos.id"))

class Tipo_dispositivo(Base):
    __tablename__ = 'tipo_dispositivo'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String)

class Punto(Base):
    __tablename__ = 'puntos'
    id = mapped_column(Integer, autoincrement=True, primary_key=True)
    x = mapped_column(Integer)
    y = mapped_column(Integer)
    z = mapped_column(Integer)
    id_dispositivo = mapped_column(ForeignKey("dispositivos.id"))
    fecha = mapped_column(DateTime, default=datetime.datetime.now)