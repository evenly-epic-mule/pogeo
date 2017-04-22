from libc.stdint cimport uint64_t
from libcpp.unordered_map cimport unordered_map
from libcpp.vector cimport vector

ctypedef vector[uint64_t] vector_uint64
ctypedef unordered_map[uint64_t, vector_uint64] cell_map
