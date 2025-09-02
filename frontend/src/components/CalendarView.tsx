import { Calendar, momentLocalizer } from 'react-big-calendar';
import moment from 'moment';
import 'react-big-calendar/lib/css/react-big-calendar.css';

const localizer = momentLocalizer(moment);

interface DailyWorkout {
  day: string;
  title: string;
}

interface CalendarViewProps {
  workouts: DailyWorkout;
}

const CalendarView = ({ workouts }: CalendarViewProps) => {
  const events = workouts.map(workout => ({
    title: workout.title,
    start: new Date(workout.day),
    end: new Date(workout.day),
    allDay: true,
  }));

  return (
    <div style={{ height: '500px' }}>
      <Calendar
        localizer={localizer}
        events={events}
        startAccessor="start"
        endAccessor="end"
      />
    </div>
  );
};

export default CalendarView;