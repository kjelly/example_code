package example
object MatchPattern {
  case class Work()
  var a: Option[Work] = None
  var b: Option[Work] = None
  def isDone = (a, b) match {
    case (Some(m), Some(n)) => {
      println("It's done")
    }
    case _ => {
      println("It's not done")
    }
  }
  def main(args: Array[String]) {
    a = Option(Work())
    isDone
    b = Option(Work())
    isDone
  }
}
