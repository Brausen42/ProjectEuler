(defn factors
  [n]
    (loop [currentNum (dec n)
           factored #{}]
      (if (< currentNum 1)
        factored
        (if (integer? (/ n currentNum))
          (recur (dec currentNum) (conj factored currentNum))
          (recur (dec currentNum) factored)))))

(defn abundant
  [n]
    (> (reduce + (factors n)) n ))

(def abundants
  (filter abundant (range 0 28500)))

(defn in?
  [x lis]
  (some #(= % x) lis))




(defn double_sums
  [nums]
  (loop [max_index (count nums)
         cur 0
         sums #{}]
    (if (= cur max_index)
      sums
      (recur max_index (inc cur) (clojure.set/union
        (let [num (get nums cur)]
          (loop [on 0
                 inner_sums #{}]
            (if (= on max_index)
              inner_sums
              (recur (inc on) (conj inner_sums (+ num (get nums on)))))))
        sums)))))






(reduce + (let [sums (double_sums (into [] abundants))]
  (filter #(not (in? % sums)) (range 1 28500))))


