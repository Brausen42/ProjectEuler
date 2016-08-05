(defn fib_with_length
  [n]
  (loop [index 1
         prev 0
         cur 1]
    (if (= (count (str cur)) n)
      index
      (recur (inc index) cur (+' prev cur)))))

(fib_with_length 1000)


