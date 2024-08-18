            """
            Inserts the predefined courses and subjects data into the MongoDB collection if not already present.
            """
            for course_name in self.data["courses"]:
                if not self.collection.find_one({"course_name": course_name}):
                    # Insert the course and its subjects into the collection
                    self.collection.insert_one({
                        "course_name": course_name,
                        "subjects": self.data["subjects"].get(course_name, [])
                    })
                    print(f"Inserted course: {course_name} with subjects: {self.data['subjects'][course_name]}")
                else:
                    print(f"Course '{course_name}' already exists in the database.")
