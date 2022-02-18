from flask_sqlalchemy import SQLAlchemy

d = SQLAlchemy()

class User(d.Model):
    id = d.Column(d.Integer, primary_key=True)
    name= d.Column(d.String(250), nullable=False)

    def serialize(self):
        return{
        "id": self.id,
        "name": self.name}

    def __repr__(self):
        return "<User %r>" % self.name
    
class Favorite(d.Model):
    id = d.Column(d.Integer, primary_key=True)
    name= d.Column(d.String(250), nullable=False)

    def serialize(self):
        return{
        "id": self.id,
        "name": self.name}

    def __repr__(self):
        return "<Favorite %r>" % self.name
    
class Person(d.Model):
    id = d.Column(d.Integer, primary_key=True)
    name= d.Column(d.String(250), nullable=False)

    def serialize(self):
        return{
        "id": self.id,
        "name": self.name}

    def __repr__(self):
        return "<Person %r>" % self.name
    
class Vehicle(d.Model):
    id = d.Column(d.Integer, primary_key=True)
    name= d.Column(d.String(250), nullable=False)

    def serialize(self):
        return{
        "id": self.id,
        "name": self.name}

    def __repr__(self):
        return "<Vehicle %r>" % self.name
    
class Planet(d.Model):
    id = d.Column(d.Integer, primary_key=True)
    name= d.Column(d.String(250), nullable=False)

    def serialize(self):
        return{
        "id": self.id,
        "name": self.name}

    def __repr__(self):
        return "<Planet %r>" % self.name
    