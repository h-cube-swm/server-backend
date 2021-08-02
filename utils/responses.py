# JSON 응답 딕셔너리를 모아둔 코드
APIOnly = {"success": True, "status": 200, "comment": "API Only"}
postOnly = {"success": False, "status": 400, "comment": "only POST allowed"}
noAPI = {
    "success": False,
    "status": 405,
    "comment": "This HTTP Method Does Not Supported",
}

ok = {"success": True, "status": 200, "comment": "OK"}
no = {"success": False, "status": 400, "comment": "NO"}

illegalArgument = {"success": False, "status": 400, "comment": "Illegal Argument"}

# Survey 관련
invalidUUID = {
    "success": False,
    "status": 400,
    "comment": "Invalid UUID(should be xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)",
}
invalidSurveyID = {"success": False, "status": 400, "comment": "Invalid Survey ID"}
surveyCannotEdit = {
    "success": False,
    "status": 400,
    "comment": "Survey Cannot Edit(Survey Status is not Editing)",
}
modifySurveySucceed = {
    "success": True,
    "status": 201,
    "comment": "Modify Survey Succeed",
}
surveyAlreadyEnd = {
    "success": True,
    "status": 200,
    "comment": "Survey Already Published or Closed",
}

# Responses 관련
createResponseSucceed = {
    "success": True,
    "status": 201,
    "comment": "Create Response Succeed",
}

invalidResultID = {
    "success": False,
    "status": 400,
    "comment": "Invalid Result ID(ID Should be Result ID, Not a Survey ID",
}
