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


(remove_element 2 '(1 2 3))

(map_to_front 0 [[1 2 3] [4 5 6]])

(insert_into 0 0 '(1 2 3))

(permute [0 1 2])

