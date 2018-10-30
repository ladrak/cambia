# cambia

Tools
1. In your opinion, what’s helpful about version control systems? What’s annoying about them?
  Version control systems help developer view a history of the changes that happend in an application. It also helps use to work "branch" experimental code, so we can make changes without introducing new bugs. Even if we do, version control systems let us quickly roll back our code to a state when we new it was functioning properly. 
  The most annoying thing about version control is having to merge different branches of code. Some times, when multiple developers are working on different changes, there comes a point in which a decision has to be made about which code is the most appropriate to integrate with the main source. These merges need to be done carefully.
  
2. What are some pros and cons of using Docker to develop, test, and deploy software?
  Docker is nice because you have a sandboxed execution environment. That means you can have confidence that errors are not caused by applications installed or other changes to your OS. When it comes to debugging this is a life saver. It also helps because if you need to test code in a specific way, it is quick and easy to start a docker container that is already preconfigured with your needs.
  
3. How do you choose which language to use for a given task? How did you choose the language for the programming exercise above?
  The choice of langues really depends on the problem domain. If I'm working on Windows, I'm using something that is .NET. If I'm working on Linux, I'm chosing something like Java, or Bash. For the task given, I used the languages given by the requirements. 


Testing Methodology
1. What’s the right role for QA in the software development process?
  QA is about testing the intregrity of a project. They perform all the tasks required by the test cases and report the results. If there are failures, it's important to dive a bit deeper into root cause, and report that back to the orginating engineering team.

2. As a QA person, you have 2 weeks to prepare before your team starts writing software. What do you do?
  I discuss the initial interface designs to build test cases; start to prepare the test enviornments; and continuesly check in with the developers about what is changing.
  
3. When is it appropriate to use automated testing? When is it appropriate to use manual testing?
  Automated testing can and should be done to start with and for any regression efforts. Manual testings should be done when there is a sense that the automations are incorrect, or when a falure is found and steps to reproduce need to be discovered. 
  
4. Your dev team has just modified an existing product by adding new features and refactoring the
code for old features. The devs claim to have written unit tests; you’re in charge of integration
testing. Dedicated teams are handling performance and security testing, so you don’t have to. As
is always the case in the real world, you don’t have time to test everything. What factors do you
think about as you decide where to focus your testing efforts? How do you decide what not to
test?
It depends on the which features are affected and in what areas of the application. If we are adding new inputs that are public facing or a new public facing API, then we need to have security testing and integration testing. Integration testing is a must, because that at least insures that the changes work, can't push broken code. We can come back to performance testings after release, but it needs to done as soon as possible to insure that the user experience is not broken. 
