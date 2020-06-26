# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
#        return Response(False, -1)
        if len(self.finish_time) == 0:
            start_time = request.arrived_at
            finish_time = start_time + request.time_to_process
            self.finish_time.append(finish_time)
            return Response(
                    was_dropped = False,
                    started_at = start_time
            )
        elif self.finish_time[-1] < request.arrived_at:
            start_time = request.arrived_at
            finish_time = start_time + request.time_to_process
            self.finish_time.append(finish_time)
            return Response(
                was_dropped=False,
                started_at=start_time
            )
        elif len(self.finish_time) < self.size:
            start_time = self.finish_time[-1]
            finish_time = start_time + request.time_to_process
            self.finish_time.append(finish_time)
            return Response(
                was_dropped=False,
                started_at=start_time
            )
        elif self.finish_time[-self.size] <= request.arrived_at:
            start_time = self.finish_time[-1]
            finish_time = start_time + request.time_to_process
            self.finish_time.append(finish_time)
            return Response(
                was_dropped=False,
                started_at=start_time
            )
        elif self.finish_time[-self.size] > request.arrived_at:
            return Response(
                was_dropped=True,
                started_at=-1
            )
        raise Exception(f"{finish_time},{request}")            


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
