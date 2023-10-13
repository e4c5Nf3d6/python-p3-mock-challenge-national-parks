import re

class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, 'name'):
            raise Exception('name cannot be changed')
        elif isinstance(name, str) and 3 <= len(name):
            self._name = name
        else:
            raise Exception('name must be a string of at least 3 characters')
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        most_visits = 0
        best_visitor = None
        for visitor in self.visitors():
            if visitor.total_visits_at_park(self) > most_visits:
                most_visits = visitor.total_visits_at_park(self)
                best_visitor = visitor
        return best_visitor
    
    @classmethod
    def most_visited(cls):
        most_visits = 0
        most_visited_park = None
        for park in list(set([trip.national_park for trip in Trip.all])):
            if park.total_visits() > most_visits:
                most_visits = park.total_visits()
                most_visited_park = park
        return most_visited_park

class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        pattern = re.compile(r'[A-Z][a-z]*\s([1-9]|[12][0-9]|3[01])[a-z]{2}')
        if isinstance(start_date, str) and len(start_date) >= 7 and pattern.fullmatch(start_date):
            self._start_date = start_date
        else:
            raise Exception('start_date must be a string of at least 7 characters in the format "September 1st"')
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        pattern = re.compile(r'[A-Z][a-z]*\s([1-9]|[12][0-9]|3[01])[a-z]{2}')
        if isinstance(end_date, str) and len(end_date) >= 7 and pattern.fullmatch(end_date):
            self._end_date = end_date
        else:
            raise Exception('end_date must be a string of at least 7 characters in the format "September 1st"')
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception('visitor must be an instance of the Visitor class')
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception('national_park must be an instance of the NationalPark class')


class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception('name must be a string between 1 and 15 characters')
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self]))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])