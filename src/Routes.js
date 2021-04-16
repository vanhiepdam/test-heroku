import config from './config';

const baseApiUrlV1 = `${config.BASE_API_URL}/api/v1`;
const routeV1 = {
    'todo': `${baseApiUrlV1}/todos`
};

const routes = {
    routeV1: routeV1
};

export default routes;
