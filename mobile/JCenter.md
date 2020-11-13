

<!--
 * @version:
 * @Author:  StevenJokess https://github.com/StevenJokess
 * @Date: 2020-11-13 19:19:52
 * @LastEditors:  StevenJokess https://github.com/StevenJokess
 * @LastEditTime: 2020-11-13 19:20:34
 * @Description:
 * @TODO::
 * @Reference:https://stackoverflow.com/questions/25137263/what-is-included-in-jcenter-repository-in-gradle
-->

Maven Central and JCenter are mostly equivalent, from a user perspective.

The reason there's 2 big repos is that Maven Central is backed by Sonatype, the company behind Maven and especially behind Nexus, a Maven repository they sell to enterprises.

JCenter is backed by JFrog, the company behind Artifactory, a competitor to Nexus. From what I remember JFrog also backed Gradle for a while, as a competitor to Maven.

So in the end it's about competing companies offering free services to try to lure customers to their higher level enterprise offerings.

Unless you have a very specific reason to use one of them, you can basically toss a coin to choose one.

---

JCenter is the place to find and share popular Apache Maven packages for use by Maven, Gradle, Ivy, SBT, etc. For the most comprehensive collection of artifacts, point your Maven at: http://jcenter.bintray.com Want to distribute your own packages through JCenter? You can link your package by clicking the "Include My Package" button. And if you're into legacy, you can even synchronize your packages directly to Maven Central.
