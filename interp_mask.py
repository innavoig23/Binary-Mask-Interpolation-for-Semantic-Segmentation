# Import libraries
import numpy as np
from scipy.ndimage import distance_transform_edt

# Function to apply interpolation between two masks
def interp_mask(mask1, mask2):
  # mask1 and mask2 must be two boolean numpy arrays that represent tumoral slices
  mask1 = np.array(mask1, dtype=bool)
  mask2 = np.array(mask2, dtype=bool)
  d1 = distance_transform_edt(mask1) - distance_transform_edt(~mask1)
  d2 = distance_transform_edt(mask2) - distance_transform_edt (~mask2)
  interpolated_mask = (d1 + d2) > 0
  interpolated_mask = np.array(interpolated_mask, dtype=np.uint8)

  return interpolated_mask
