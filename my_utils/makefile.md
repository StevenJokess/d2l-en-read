

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 22:32:02
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 22:34:26
 * @Description:
 * @TODO::
 * @Reference:https://en.wikipedia.org/wiki/Makefile
-->

File containing a set of directives used with the make build automation tool

It lists the other files that the targets depend on, called the prerequisites of the target, and may also give a recipe to use to create or update the targets.



Most often, the makefile directs Make on how to compile and link a program. A makefile works upon the principle that files only need recreating if their dependencies are newer than the file being created/recreated. The makefile is recursively carried out (with dependency prepared before each target depending upon them) until everything has been updated (that requires updating) and the primary/ultimate target is complete. These instructions with their dependencies are specified in a makefile. **If none of the files that are prerequisites have been changed since the last time the program was compiled, no actions take place. For large software projects, using Makefiles can substantially reduce build times if only a few source files have changed.**

Using C/C++ as an example, when a C/C++ source file is changed, it must be recompiled. If a header file has changed, each C/C++ source file that includes the header file must be recompiled to be safe. Each compilation produces an object file corresponding to the source file. Finally, if any source file has been recompiled, all the object files, whether newly made or saved from previous compilations, must be linked together to produce the new executable program.[1]
