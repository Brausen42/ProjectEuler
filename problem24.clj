(defn remove_element
  [n lis]
  (loop [front []
         [h & tail] lis]
    (if (= h n)
      (concat (reverse front) tail)
      (recur (cons h front) tail))))

(defn insert_into
  [n i lis]
  (loop [front []
         cur 0
         [h & tail] lis]
    (if (= cur i)
      (if (nil? h)
        (reverse (cons n front))
        (concat (reverse (cons h (cons n front))) tail))
      (recur (cons h front) (inc cur) tail))))

(defn map_to_front
  [h lis]
  (map #(cons h %) lis))

(defn permute
  [lis]
  (if (<= (count lis) 1)
    [lis]
    (loop [[h & tail] lis
           perms []]
      (if (empty? tail)
        (concat perms (map_to_front h (permute (remove_element h lis))))
        (recur tail (concat perms (map_to_front h (permute (remove_element h lis)))))))))

(defn other_permute
  [lis]
  (loop [[h & tail] lis
         length 0
         perms [[]]]
    (if (nil? h)
      perms
      (recur tail (inc length) (loop [new_perms []
                                      index 0]
                                 (if (> index length)
                                   new_perms
                                   (recur (concat new_perms (map #(into [] (insert_into h index %)) perms)) (inc index))))))))


(remove_element 2 '(1 2 3))

(map_to_front 0 [[1 2 3] [4 5 6]])

(insert_into 0 0 '(1 2 3))

(permute [0 1 2 3])

(get [1 2 3] 0)

(time (other_permute [0 1 2 3 4 5 6 7 8 9]))

; Not mine but I couldn't get both efficiency and lexicographic properties and also this approach is neat
(let [! (fn [n] (reduce * (range 1 (inc n))))]
  (loop [available-digits (range 10)
         num 1000000
         current-digit 0
         init 9
         result []]
    (let [f (! init)]
      (cond
        (= 0 init)
        (apply str (concat result available-digits))

        (< f num) (recur available-digits
                         (- num f)
                         (inc current-digit)
                         init
                         result)

        :else (recur (concat (take current-digit available-digits)
                             (drop (inc current-digit) available-digits))
                     num
                     0
                     (dec init)
                     (conj result (nth available-digits current-digit)))))))
