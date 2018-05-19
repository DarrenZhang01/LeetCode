Class Solution(object):
    """
    plusOne
    """
    def plusOne (self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # First convert the orginal list into a number
        value = 0
        time = 1
        for i in range(len(digits)):
            value += time * digits[len(digits) - i - 1]
            time *= 10
        value += 1
        # Second convert the result into a List
        list_ = []
        for i in str(value):
            list_.append(int(i))
        return list
