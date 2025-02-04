
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

reference_image_path = "Test Images/Component Deffects/A2/ref.png"  # Replace with the path to your reference image
source_image_path = "Test Images/Component Deffects/A2/source.png"        # Replace with the path to your source image

# Load reference and source images
reference_image = cv2.imread(reference_image_path, cv2.IMREAD_COLOR)
source_image = cv2.imread(source_image_path, cv2.IMREAD_COLOR)


def warp_image_to_reference(reference_image,source_image,ref_gray,src_gray):
    

    # Initialize SIFT detector
    sift = cv2.SIFT_create()

    # Detect keypoints and descriptors
    keypoints_ref, descriptors_ref = sift.detectAndCompute(ref_gray, None)
    keypoints_src, descriptors_src = sift.detectAndCompute(src_gray, None)

    # Use FLANN-based matcher
    index_params = dict(algorithm=1, trees=5)  # FLANN_INDEX_KDTREE
    search_params = dict(checks=50)  # Adjust for speed vs accuracy

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptors_src, descriptors_ref, k=2)

    # Apply Lowe's ratio test to filter good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Ensure enough matches are found
    if len(good_matches) > 10:
        # Extract matched keypoints
        src_pts = np.float32([keypoints_src[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        ref_pts = np.float32([keypoints_ref[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        # Compute the homography matrix
        H, mask = cv2.findHomography(src_pts, ref_pts, cv2.RANSAC, 5.0)

        # Warp the source image to the reference image's perspective
        warped_image = cv2.warpPerspective(source_image, H, (ref_gray.shape[1], ref_gray.shape[0]))
        return warped_image
        
    

    else:
        print("Not enough matches found!")
        return None
    

# Example usage


def detect_anomaly(reference_image,source_image):

    # Convert images to grayscale
    ref_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    src_gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)

    warped_image = warp_image_to_reference(reference_image,source_image,ref_gray,src_gray)
    warped_image_gray=cv2.cvtColor(warped_image, cv2.COLOR_BGR2GRAY)

    # Define kernel size for dilation (controls how many neighbors to include)
    kernel = np.ones((3, 3), np.uint8)  # Adjust the kernel size as needed

    # Create a binary mask for black pixels
    black_pixels = warped_image_gray == 0

    # Dilate the mask to include neighboring pixels
    dilated_mask = cv2.dilate(black_pixels.astype(np.uint8), kernel, iterations=1)

    # Replace the dilated region with the reference image pixels
    warped_image_gray[dilated_mask == 1] = ref_gray[dilated_mask == 1]


    # Compute absolute difference between the two images
    difference = cv2.absdiff(warped_image_gray, ref_gray)
    # Apply thresholding to highlight the differences
    _, thresholded = cv2.threshold(difference, 60, 255, cv2.THRESH_BINARY)
    # Find contours of the differences
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw rectangles around the differing regions


    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        warped_image = cv2.cvtColor(np.array(warped_image), cv2.COLOR_BGR2RGB)
        cv2.rectangle(warped_image, (x, y), (x + w, y + h), (255, 0, 0), 5)

    # warped_image = cv2.cvtColor(np.array(warped_image), cv2.COLOR_RGB2BGR)

    return warped_image

warped_image = detect_anomaly(reference_image,source_image)

cv2.imshow("source_img",warped_image)

# Wait for the user to press a key
cv2.waitKey(0)

# # Close all windows
cv2.destroyAllWindows()