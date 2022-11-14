def detectCollision(A, B):
    if A.x < B.x + B.w and A.x + A.w > B.x and A.y < B.y + B.h and A.h + A.y > B.y:
        # print("Collision Detected Between Two Objects")
        return True
    return False


def detect_mouse_col(A, B):
    if A[0] < B.x + B.w and A[0] > B.x and A[1] < B.y + B.h and A[1] > B.y:
        # print("Mouse Collision Detected")
        return True
    return False
