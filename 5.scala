object Solution {
  def longestPalindrome(s: String): String = {
    val matrix: Array[Array[Int]] = new Array[Array[Int]](s.length)
    for (idx <- 0 until s.length) {
      matrix.update(idx, new Array[Int](s.length))
    }

    var start = 0
    var end = 0
    var currMax = 1

    for (idx <- 0 until s.length) {
      matrix.apply(0).update(idx, 1)

      if (idx + 1 < s.length) {
        if (s.charAt(idx) == s.charAt(idx + 1)) {
          matrix.apply(1).update(idx, 2)

          if (currMax < 2) {
            start = idx
            end = idx + 1
          }
        }
        else {
          matrix.apply(1).update(idx, 0)
        }
      }
    }


    for (i <- 2 until s.length) {
      for (j <- 0 until s.length) {
        if (j + i < s.length) {
          if (s.charAt(j) == s.charAt(j+i) && matrix.apply(i - 2).apply(j + 1) != 0) {
            matrix.apply(i).update(j, matrix.apply(i - 2).apply(j + 1) + 2)

            if (currMax < matrix.apply(i).apply(j)) {
              currMax = matrix.apply(i).apply(j)
              start = j
              end = i + j
            }
          }
          else {
            matrix.apply(i).update(j, 0)
          }
        }
      }
    }

    // matrix.foreach(x => println(x.mkString(", ")))

    s.substring(start, end + 1)
  }
}