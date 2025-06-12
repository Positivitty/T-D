import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import {
  AppShell,
  Text,
  NavLink,
  Container,
  MantineProvider,
} from "@mantine/core";
import { IconBox, IconUsers, IconClipboardList } from "@tabler/icons-react";
import { ContainerList } from "./components/containers/ContainerList";
import { CustomerList } from "./components/customers/CustomerList";
import { LogEntryList } from "./components/log-entries/LogEntryList";

function App() {
  return (
    <MantineProvider>
      <Router>
        <AppShell
          header={{ height: 60 }}
          navbar={{ width: 300, breakpoint: "sm" }}
          padding="md"
        >
          <AppShell.Header>
            <Container style={{ height: "100%", display: "flex", alignItems: "center" }}>
              <Text size="xl" fw={700}>
                T@D Rolloff Container Tracker
              </Text>
            </Container>
          </AppShell.Header>

          <AppShell.Navbar p="md">
            <NavLink
              component={Link}
              to="/"
              label="Containers"
              leftSection={<IconBox size={20} />}
            />
            <NavLink
              component={Link}
              to="/customers"
              label="Customers"
              leftSection={<IconUsers size={20} />}
            />
            <NavLink
              component={Link}
              to="/log-entries"
              label="Log Entries"
              leftSection={<IconClipboardList size={20} />}
            />
          </AppShell.Navbar>

          <AppShell.Main>
            <Container>
              <Routes>
                <Route path="/" element={<ContainerList />} />
                <Route path="/customers" element={<CustomerList />} />
                <Route path="/log-entries" element={<LogEntryList />} />
              </Routes>
            </Container>
          </AppShell.Main>
        </AppShell>
      </Router>
    </MantineProvider>
  );
}

export default App;
