# JSON 응답 딕셔너리를 모아둔 코드

APIOnly = {"success": True, "status": 200, "comment": "API Only"}
postOnly = {"success": False, "status": 400, "comment": "only POST allowed"}

ok = {"success": True, "status": 200, "comment": "OK"}
no = {"success": False, "status": 400, "comment": "NO"}

illegalArgument = {"success": False, "status": 400, "comment": "Illegal argument"}