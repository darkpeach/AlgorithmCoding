class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        waitList = path.split("/")
        resultList = [""]
        for item in waitList:
            if item == "..":
                if resultList != [""]:
                    resultList.pop()
            elif item != "." and item != "":
                resultList.append(item)
        if resultList == [""]:
            resultList.append("")
        result = "/".join(resultList)
        return result