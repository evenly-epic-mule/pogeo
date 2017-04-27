from .geo.s2loop cimport S2Loop


cdef class Loop:
    cdef S2Loop loop
    cdef readonly double south, east, north, west