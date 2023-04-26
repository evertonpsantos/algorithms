def study_schedule(permanence_period, target_time):
    try:
        student_count = 0

        for entry_time, exit_time in permanence_period:
            if entry_time <= target_time <= exit_time:
                student_count += 1

        return student_count

    except TypeError:
        return None
