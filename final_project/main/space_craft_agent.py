from final_project.main.communication_service import CommunicationService


class SpaceCraftAgent:
    def __init__(self):
        self.status = "Idle"
        self.messaging_service = CommunicationService()

    def status_update(self) -> str:
        """
        Provide updates on the spacecraft's status.
        """
        return f"Spacecraft status: {self.status}"

    def receive_command(self, command: str) -> str:
        """
        React to commands and update the spacecraft's status.
        """
        if command == "LAUNCH":
            self.status = "Launched"
        elif command == "LAND":
            self.status = "Landed"
        else:
            self.status = "Unknown Command"
        return f"Command received: {command}, new status: {self.status}"

    def connect(self, address: str) -> bool:
        return self.messaging_service.connect(address)

    def disconnect(self) -> bool:
        return self.messaging_service.disconnect()

    def send_message(self, message: str) -> bool:
        return self.messaging_service.send_message(message)

    def receive_message(self) -> str:
        return self.messaging_service.receive_message()