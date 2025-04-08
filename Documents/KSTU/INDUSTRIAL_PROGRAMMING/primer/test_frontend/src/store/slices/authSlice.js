import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { loginUser } from '../services/authServices';

export const login = createAsyncThunk(
    'auth/login',
    async ({ email, password }, { rejectWithValue }) => {
        try {
            debugger
            const data = await loginUser(email, password);
            if (data.access_token) {
                localStorage.setItem("accessToken", data.access_token);
                return data;
            } else {
                debugger
                return rejectWithValue("Неизвестная ошибка авторизации.");
            }
        } catch (err) {
            return rejectWithValue(err.response?.data?.detail || "Ошибка сервера. Попробуйте снова.");
        }
    }
);

const authSlice = createSlice({
    name: 'auth',
    initialState: {
        isLoggedIn: false,
        error: null,
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(login.pending, (state) => {
                state.error = null; // очищаем ошибку при новом запросе
            })
            .addCase(login.fulfilled, (state, action) => {
                state.isLoggedIn = true;
                state.error = null;
            })
            .addCase(login.rejected, (state, action) => {
                state.error = action.payload || "Произошла ошибка";
            });
    },
});

export const authReducer = authSlice.reducer;
