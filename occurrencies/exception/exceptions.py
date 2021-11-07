

class DatabaseIntegrationError(Exception):
    message = "Can't connect to the database"
    status_code = 500

class NotFoundException(Exception):
    message = "No resource found"
    status_code = 404
