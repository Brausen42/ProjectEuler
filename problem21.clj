(defn factors
  [n]
    (loop [currentNum (dec n)
           factored #{}]
      (if (< currentNum 1)
        factored
        (if (integer? (/ n currentNum))
          (recur (dec currentNum) (conj factored currentNum))
          (recur (dec currentNum) factored)))))

(defn amicable
  [n]
    (let [factor_sums (map #(reduce + %) (map factors (range 0 n)))]
      (loop [currentNum 1
             amicable_nums #{}]
        (if (>= currentNum n)
          amicable_nums
          (let [cur (nth factor_sums currentNum)]
            (if (< cur n)
              (if (and (= currentNum (nth factor_sums cur)) (not= currentNum cur))
                (recur (inc currentNum) (conj (conj amicable_nums currentNum) cur))
                (recur (inc currentNum) amicable_nums))
              (recur (inc currentNum) amicable_nums)))))))

(reduce + (amicable 10000))
