class Node(object):
    def __init__(self, course_num):
        self.course_num = course_num
        self.prereqs = set()

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # add all the courses to the graph
        courses = []
        for i in range(numCourses):
            courses.append(Node(i))
        
        # iterate through the prereqs list and add edges to connect the necessary nodes
        for prereq in prerequisites:
            if (prereq[0] in courses[prereq[1]].prereqs): # early cycle
                return False

            courses[prereq[0]].prereqs.add(prereq[1])
        
        # traverse the graph using DFS to look for long-range cycles
        for course in courses:
            visited = set()
            done = set()
            if self.traverseGraph(course, visited, done, courses) == False:
                return False
        
        return True
    
    def traverseGraph(self, root, visited, done, courses):
        # base case 1
        if root in visited:
            return False
                
        visited.add(root)

        for neighbor in root.prereqs:
            if neighbor in done:
                continue

            result = self.traverseGraph(courses[neighbor], visited, done, courses)
            if result == True:
                done.add(neighbor)
            else:
                return False
        
        done.add(root)
        return True