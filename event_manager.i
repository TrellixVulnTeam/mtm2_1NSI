%module event_manager
%{
#include "event_manager.h"
#include "date.h"
%}
EventManager createEventManager(Date date);
void destroyEventManager(EventManager em);
EventManagerResult emAddEventByDate(EventManager em, char* event_name, Date date, int event_id);
int emGetEventsAmount(EventManager em);
char* emGetNextEvent(EventManager em);
void emPrintAllEvents(EventManager em, const char* file_name);
int dateCompare(Date date1, Date date2);

