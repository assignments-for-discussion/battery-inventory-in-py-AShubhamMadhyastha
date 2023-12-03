def count_batteries_by_health(present_capacities):
    counts={}
    for i in present_capacities:
        soh=int(100*i/120)  #soh calculation of all present capacities
        
        #classification
        if soh<=100 and soh>=80:
          counts["healthy"]=1+counts.get("healthy",0)
        elif soh<80 and soh>=62:
          counts["exchange"]=1+counts.get("exchange",0)
        else:
          counts["failed"]=1+counts.get("failed",0)
    return counts


def test_bucketing_by_health():
      print("Counting batteries by SoH...\n")
      present_capacities = [113, 116, 80, 95, 92, 70]
      counts = count_batteries_by_health(present_capacities)
      assert(counts["healthy"] == 2)
      assert(counts["exchange"] == 3)
      assert(counts["failed"] == 1)
      print("Done counting :)")


if __name__ == '__main__':
      test_bucketing_by_health()
