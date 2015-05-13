import numpy as np
import cPickle
import heapq
import os
from IPython.core.debugger import Tracer
import scipy.io as scio

def mkdir_if_missing(output_dir):
  """
  def mkdir_if_missing(output_dir)
  """
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def save_variables(pickle_file_name, var, info, overwrite = False):
  """
    def save_variables(pickle_file_name, var, info, overwrite = False)
  """
  if os.path.exists(pickle_file_name) and overwrite == False:
    raise Exception('{:s} exists and over write is false.'.format(pickle_file_name))
  # Construct the dictionary
  assert(type(var) == list); assert(type(info) == list);
  d = {}
  for i in xrange(len(var)):
    d[info[i]] = var[i]
  with open(pickle_file_name, 'wb') as f:
    cPickle.dump(d, f, cPickle.HIGHEST_PROTOCOL)

def load_variables(pickle_file_name):
  """
  d = load_variables(pickle_file_name)
  Output:
    d     is a dictionary of variables stored in the pickle file.
  """
  if os.path.exists(pickle_file_name):
    with open(pickle_file_name, 'rb') as f:
      d = cPickle.load(f)
    return d
  else:
    raise Exception('{:s} does not exists.'.format(pickle_file_name))
