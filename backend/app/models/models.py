from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from .base import Base


class ContainerStatus(str, enum.Enum):
    AVAILABLE = "available"
    IN_USE = "in_use"
    NEEDS_PICKUP = "needs_pickup"
    IN_MAINTENANCE = "in_maintenance"


class Container(Base):
    id = Column(Integer, primary_key=True, index=True)
    container_number = Column(String, unique=True, index=True, nullable=False)
    status = Column(Enum(ContainerStatus), default=ContainerStatus.AVAILABLE)
    location = Column(String)
    notes = Column(Text)
    
    # Relationships
    current_customer_id = Column(Integer, ForeignKey("customer.id"), nullable=True)
    current_customer = relationship("Customer", back_populates="current_containers")
    log_entries = relationship("LogEntry", back_populates="container")


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String)
    phone = Column(String)
    job_site_info = Column(Text)
    
    # Relationships
    current_containers = relationship("Container", back_populates="current_customer")
    log_entries = relationship("LogEntry", back_populates="customer")


class LogEntryType(str, enum.Enum):
    DROPOFF = "dropoff"
    PICKUP = "pickup"
    MAINTENANCE = "maintenance"


class LogEntry(Base):
    id = Column(Integer, primary_key=True, index=True)
    container_id = Column(Integer, ForeignKey("container.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    action = Column(Enum(LogEntryType), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    notes = Column(Text)
    
    # Relationships
    container = relationship("Container", back_populates="log_entries")
    customer = relationship("Customer", back_populates="log_entries") 