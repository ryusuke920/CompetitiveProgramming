class Rect:
  def init(self, x, y, w, h):
    self.x1 = x
    self.y1 = y
    self.x2 = x + w
    self.y2 = y + h
    self.w = w
    self.h = h

  def overlap(self, b):
    return max(self.x1, b.x1) < min(self.x2, b.x2) and max(self.y1, b.y1) < min(self.y2, b.y2)

  def subtract_by(self, b):
    if self.overlap(b):
      rooms = []
      if (self.x1 < b.x1 and b.x1 < self.x2) and max(self.y1, b.y1) < min(self.y2, b.y2):
        rooms.append(Rect(self.x1, self.y1, b.x1 - self.x1, self.h))

      if (self.x1 < b.x2 and b.x2 < self.x2) and max(self.y1, b.y1) < min(self.y2, b.y2):
        rooms.append(Rect(b.x2, self.y1, self.x2 - b.x2, self.h))

      if (self.y1 < b.y1 and b.y1 < self.y2) and max(self.x1, b.x1) < min(self.x2, b.x2) :
        rooms.append(Rect(self.x1, self.y1, self.w, b.y1 - self.y1))

      if (self.y1 < b.y2 and b.y2 < self.y2) and max(self.x1, b.x1) < min(self.x2, b.x2) :
        rooms.append(Rect(self.x1, b.y2, self.w, self.y2 - b.y2))
      return rooms

    else:
      return [self]

  def include(self, b):
    return self.x1 <= b.x1 and b.x2 <= self.x2 and self.y1 <= b.y1 and b.y2 <= self.y2

  def larger_than(self, w, h):
    # 座標は関係なく、図形として入るかどうか
    return w <= self.w and h <= self.h

  def str(self):
    return "({}, {}, {}, {})".format(self.x1, self.y1, self.w, self.h)

def put_rect(input_rects, roomsORIG=[Rect(0, 0, 1024, 10000)]):
  '''
  空間にBottom-Left法で矩形を配置しその位置のリストを返す。

  Parameters
  ----------
  input_rects: [(int, int)]
      (width, height)で表される入力矩形のリスト
  rooms: [(int, int, int, int)]
      (x, y, width, height)で表される空白矩形リスト。配置可能空間を示す。

  Returns
  -------
  rects: [int, int, int, int]
      (x, y, width, height)で表される配置した矩形リスト
  rooms: [int, int, int, int]
      (x, y, width, height)で表される空白矩形リスト
  '''

  # 空白矩形と比較し、配置可能な空白を探索
  rects = []
  uniq_rooms = list(roomsORIG)
  for input_rect in input_rects:
    for i in range(len(uniq_rooms)):
      room = uniq_rooms[i]
      if room.larger_than(input_rect[0], input_rect[1]): #このrectに配置可能
        new_rect = Rect(room.x1, room.y1, input_rect[0], input_rect[1])
        rects.append(new_rect)
        break

    # すべての空白矩形から subtractする
    new_rooms = []
    for room in uniq_rooms:
      new_rooms += room.subtract_by(new_rect)
    new_rooms = sorted(new_rooms, key=lambda x:x.y1) # 結局総当たりするので意味ないが、将来効率化を考えソート

    # 重複削除 総当たり
    uniq_rooms = []
    for r_i in new_rooms:
      include_flg = False
      for r_j in new_rooms:
        if r_i == r_j: continue
        if r_j.include(r_i):
          include_flg = True
          break
      if not include_flg:
        # print("{} は他のどれにも含まれない".format(r_i))
        uniq_rooms.append(r_i)
    # 低い順（左にある順）に並び替え
    new_rooms = sorted(new_rooms, key=lambda a:a.x1)
    uniq_rooms = sorted(new_rooms, key=lambda a:a.y1)

  return (rects, uniq_rooms)



img_list = [(300, 350), (200, 300), (400, 400), (150, 250), (250, 400)]
rects, rooms = put_rect(img_list)
for rect in rects:
  print(rect)