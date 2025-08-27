# Word Challenge - English Learning App

This is a web application designed to help users learn English words through a fun and interactive word challenge. Users can register for an account, take quizzes, and track their progress. The application is built with a modern tech stack and is designed to be a Progressive Web App (PWA) for a better user experience.

## Features

-   **User Authentication:** Secure user registration and login system.
-   **Word Challenge Quiz:** A multiple-choice quiz where users are given an English word and must select the correct Chinese translation.
-   **Progress Tracking:** The application records whether each answer is correct or incorrect, helping users to focus on words they find difficult.
-   **10-Word Sessions:** Each quiz session consists of 10 words to keep the learning process focused and engaging.
-   **Progressive Web App (PWA):** The app can be "installed" on a device and offers some offline capabilities.

## Tech Stack

-   **Framework:** [Next.js](https://nextjs.org/)
-   **UI Library:** [React](https://reactjs.org/)
-   **Language:** [TypeScript](https://www.typescriptlang.org/)
-   **Styling:** [Tailwind CSS](https://tailwindcss.com/)
-   **Database/ORM:** [Prisma](https://www.prisma.io/) with [SQLite](https://www.sqlite.org/index.html)
-   **Authentication:** `bcrypt` for password hashing.
-   **PWA:** `next-pwa` for Progressive Web App support.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing.

### Prerequisites

-   [Node.js](https://nodejs.org/) (v20 or later recommended)
-   [pnpm](https://pnpm.io/) package manager

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    ```bash
    pnpm install
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root of the project and add the following line. This tells Prisma where to find the SQLite database file.
    ```
    DATABASE_URL="file:./prisma/dev.db"
    ```

4.  **Set up the database:**
    Run the following command to apply the database schema and create the `dev.db` file.
    ```bash
    pnpm prisma migrate dev
    ```

5.  **Seed the database (Optional):**
    The project includes a seed script to populate the database with initial data.
    ```bash
    pnpm prisma db seed
    ```
    *Note: The seed script is configured in `package.json` under the `prisma.seed` key.*

### Running the Development Server

Once the setup is complete, you can start the development server:

```bash
pnpm dev
```

The application will be available at [http://localhost:3000](http://localhost:3000).

## Deployment

The project is configured for deployment to an AWS EC2 instance. The deployment process is automated with a shell script.

-   **Deployment Script:** The `scripts/deploy.sh` script handles the entire process: building the project, packaging the necessary files, transferring them to the server, and restarting the application.
-   **Server Setup:**
    -   The application runs as a `systemd` service, defined in `deploy/wordgame.service`. It runs on port 3001.
    -   [Nginx](https://www.nginx.com/) is used as a reverse proxy to handle incoming traffic, as configured in `deploy/nginx.conf`. It maps the domain to the running application.

To deploy, you will need to configure the variables in `scripts/deploy.sh` (like `VM_HOST` and the path to your SSH key) and then run the script:

```bash
bash scripts/deploy.sh
```
