import { parseISO, format } from "date-fns";

export const formatter = date => {
  const parseDate = parseISO(date);

  const formattedDate = format(parseDate, "dd/MM/yyyy");

  return formattedDate;
};
