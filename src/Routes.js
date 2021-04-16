const baseApiUrl = 'http://localhost:8000';
const baseApiUrlV1 = `${baseApiUrl}/api/v1`;
const routeV1 = {
    'todo': `${baseApiUrlV1}/todos`
};

const routes = {
    routeV1: routeV1
};

export default routes;
