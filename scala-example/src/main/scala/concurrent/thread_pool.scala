package example.thread_pool

import java.net.{ Socket, ServerSocket }
import java.util.concurrent.{ Executors, ExecutorService }
import java.util.Date

class ThreadPoolDemo(poolSize: Int) extends Runnable {
  val pool: ExecutorService = Executors.newFixedThreadPool(poolSize)
  def run() {
    for (i <- 1 to 200) {
      pool.execute(new Handler(i))
    }
    pool.shutdown()
  }
}

class Handler(num: Int) extends Runnable {
  def message = (Thread.currentThread.getName() + ": ")

  def run() {
    println(message + num.toString)
  }
}

object Main {
  def main(args: Array[String]) {
    new ThreadPoolDemo(5).run
  }
}

