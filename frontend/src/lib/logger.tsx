export default class {
    public static debug(data: unknown = ""): void {
        // eslint-disable-next-line no-console
        console.debug(data);
    }

    public static info(data: unknown = ""): void {
        // eslint-disable-next-line no-console
        console.log(data);
    }

    public static warn(data: unknown = ""): void {
        // eslint-disable-next-line no-console
        console.warn(data);
    }

    public static error(data: unknown = ""): void {
        // eslint-disable-next-line no-console
        console.error(data);
    }
}
