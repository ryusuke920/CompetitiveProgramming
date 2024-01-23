

ScoreType evaluate_action(const Action& a) {
    ScoreType ret = 0;
    int oc = a.overlap_count;
    int oc2 = oc * oc;
    ret += a.overlap_weight * oc2;
    ret += a.expand_state_weight * count_expand_tile(a);
    return ret;
  }

