name := "hello"

version := "1.0"

scalaVersion := "2.10.3"

resolvers += "Typesafe Repository" at "http://repo.typesafe.com/typesafe/releases/"

// libraryDependencies +=
//       "com.typesafe.akka" %% "akka-actor" % "2.3.2"

libraryDependencies +=
      "org.scala-lang" % "scala-actors" % "2.10.0"

libraryDependencies += "org.scala-lang" % "scala-swing" % "2.10+"
