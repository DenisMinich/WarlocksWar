class ElasticCollissionProcessor:
    @staticmethod
    def process_collission(first, second):
        pass

    @staticmethod
    def get_resistance_vector(self, widget):
        intersection = Collidable.get_intersection(self, widget)
        affection_zone = self._get_affection_zone(intersection)
        result = self._calculate_resistance_vector(affection_zone)
        return result

   @staticmethod
    def get_velocity_after_collission(first, second):
        collission_vector_x = second.get_resistance_vector(first)
        collission_vector_y = collission_vector_x.rotate(90)
        v1, v2 = first.velocity, second.velocity
        system_speed = Vector(v2)
        v1, v2 = Vector(v1) - system_speed, Vector(v2) - system_speed
        system_rotate_angle = Vector(1, 0).angle(collission_vector_x)
        v1a, v1b = Vector(v1).rotate(system_rotate_angle)
        mass_ratio = 0 if not second.mass else first.mass / second.mass
        u1a_1, u1a_2 = Collidable.solve_quadratic_equation(
            a = mass_ratio + 1,
            b = -2 * mass_ratio * v1a,
            c = (mass_ratio - 1) * v1a ** 2)
        u1a = u1a_1 if u1a_1 != v1a else u1a_2
        u1b = v1b
        u2a = mass_ratio * (v1a - u1a)
        u2b = 0
        u1 = Vector(u1a, u1b).rotate(-system_rotate_angle)
        u2 = Vector(u2a, u2b).rotate(-system_rotate_angle)
        u1, u2 = u1 + system_speed, u2 + system_speed
        return u1, u2

    @staticmethod
    def solve_quadratic_equation(a, b, c):
        D = b ** 2 - 4 * a * c
        return (-b + D ** .5) / (2 * a), (-b - D ** .5) / (2 * a)
