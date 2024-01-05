def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "image": user["image"],
        "face_encoding": user["face_encoding"],
        "verified": user["verified"],
        "password": user["password"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }

def userResponseEntity(user) -> dict:
    return {
        "id": str(user["id"]),
        "name":  user["name"],
        "email": user["email"],
        "image": user["image"],
        "face_encoding": user["face_encoding"],
        "verified": user["verified"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }


def embeddedUserResponse(user) -> dict: 
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "image": user["image"]
    }

def userListEntity(users) -> list: 
    return [userEntity(user) for user in users]