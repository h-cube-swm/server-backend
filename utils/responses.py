# JSON 응답 딕셔너리를 모아둔 코드
APIOnly = {"success": True, "status": 200, "comment": "API Only"}
postOnly = {"success": False, "status": 400, "comment": "only POST allowed"}

ok = {"success": True, "status": 200, "comment": "OK"}
no = {"success": False, "status": 400, "comment": "NO"}

illegalArgument = {"success": False, "status": 400, "comment": "Illegal Argument"}

# Users
illegalUID = {"success": False, "status": 400, "comment": "Illegal UID"}
createUserSucceed = {"success": True, "status": 200, "comment": "create user succeed"}
modifyUserSucceed = {"success": True, "status": 200, "comment": "modify user succeed"}
deleteUserSucceed = {"success": True, "status": 200, "comment": "delete user succeed"}
userAlreadyRegistered = {
    "success": False,
    "status": 403,
    "comment": "User(UID) has already registered.",
}